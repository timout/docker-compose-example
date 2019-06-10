### Simple example for docker-compose and python usage

Very simple example to show how to use docker-compose and python app for integeration testing.  
#### Parts  
- app: python app  
- test: python integration tests  
- cassandra: cassandra db  
- redis: redis db  
- wait: https://github.com/ufoscout/docker-compose-wait/releases/download/2.5.0/wait (to wait when env is ready)
- watchdog: to rerun tests when any *.py was changed

#### Usage
- build: docker-compose build
- start: docker-compose up
- stop: docker-compose stop