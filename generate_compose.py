import os
import yaml
import argparse

# 명령줄 인수 파서 설정
parser = argparse.ArgumentParser(description='Generate Docker Compose file for a specific user.')
parser.add_argument('user_id', type=int, help='User ID to generate unique Docker Compose file')
args = parser.parse_args()

# 사용자별 고유 ID
user_id = args.user_id

# 기본 포트 번호 (사용자별로 고유하게 변경)
base_port = 10000 * user_id

# 동적으로 생성할 docker-compose 내용
compose_content = {
    'version': '3.5',
    'services': {
        'sandbox-hdp-{user_id}': {
            'image': 'hortonworks/sandbox-hdp:2.6.5',
            'container_name': f'sandbox-hdp-{user_id}',
            'hostname': f'sandbox-hdp.hortonworks.com',
            'networks': {
                f'cda-{user_id}': {
                    'aliases': [f'sandbox-hdp.hortonworks.com']
                }
            },
            'privileged': True
        },
        'sandbox-proxy-{user_id}': {
            'image': 'hortonworks/sandbox-proxy:1.0',
            'container_name': f'sandbox-proxy-{user_id}',
            'links': [f'sandbox-hdp-{user_id}'],
            'volumes': [
                './assets/nginx.conf:/etc/nginx/nginx.conf',
                './assets/sandbox/proxy/conf.d:/etc/nginx/conf.d',
                './assets/sandbox/proxy/conf.stream.d:/etc/nginx/conf.stream.d'
            ],
            'networks': [f'cda-{user_id}'],
            'ports': [
                f'{user_id + 8080}:8080'
            ]
        }
    },
    'networks': {
        f'cda-{user_id}': {
            'driver': 'bridge'
        }
    }
}

# docker-compose 파일 저장 경로
compose_file_path = f'docker-compose-{user_id}.yml'

# docker-compose 파일 생성
with open(compose_file_path, 'w') as file:
    yaml.dump(compose_content, file, default_flow_style=False)

print(f'Docker Compose file generated: {compose_file_path}')
