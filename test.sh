docker compose build
docker compose up -d
cd server2
docker build -t test_server_2
docker run -itd --network=test_bridge -p 5501:5500 --name test_server_2 test_server_2 python3 main.py