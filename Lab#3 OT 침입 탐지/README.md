# OT/ICS Security Lab

OT/ICS 보안 구축 실습 기록

OT Security | Network Segmentation | Modbus | IDS

---

## Lab 03 - OT 침입 탐지

### 실습 내용

지난번에 만든 OpenPLC 프로그램에 Python으로 제작한 공격 파일로 공격을 진행해봤다.

Suricata를 사용해 OpenPLC에서 IDS(침입탐지시스템)를 재현해보았다.
- Suricata: 6.0.4
- interface: enp0s3 (192.168.31.177/24)
- Modbus Port: 502

공격자 파일은 `attack.py` 로 만들었다. pymodbus로 OpenPLC에 접속하여 값을 읽고 변경하는 공격 파일이다.

### tcpdump + suricata
로그는 tcpdump로 잡았다. 컴퓨터 내부에서 도는 루프백 패킷이라서 `enp0s3`으로 잡히지 않고 `lo`로 잡아야 했다.

suricata 실행은 이렇게 했다.

```
sudo suricata -c /etc/suiricata/suricata.yaml -r /tmp/modbus.pcap -k none
```

### 공격 실행
`attack.py`를 실행해서 OpenPLC에 Modbus 공격을 가했다.

<img width="395" height="82" alt="image" src="https://github.com/user-attachments/assets/0af5ed8f-df30-4fb5-8c50-11efb6ba6875" />

### 패킷 분석
`fast.log`를 열어봤다. suricata가 IDS역할을 수행하여 잡아낸 로그이다.
<img width="1282" height="263" alt="image" src="https://github.com/user-attachments/assets/3e7ad698-16dd-4fa0-a6c1-0b0ba86ff5e9" />
```
[**] [1:1000001:1] OT - Modbus Access Attempt [**]
```

| 필드 | 값 | 의미 |
| --- | --- | --- |
| SID | 1000001 | 내가 만든 룰 1번 |
| 출발지 | 192.168.31.177:44074 | 공격자 |
| 목적지 | 192.168.31.177:502 | OpenPLC Modbus 포트 |

### 트러블슈팅

| 문제 | 원인 | 해결 |
| --- | --- | --- |
| read_holding_registers() 구문 오류 | 구버전 pymodbus 키워드 사용  | read_holding_registers(address=0, count=1)로 변경 |
|enp0s3으로 잡으면 0개|내 컴퓨터 -> 내 컴퓨터 패킷은 lo로 감|tcpdump -i lo로 잡기|
|fast.log 비어있음|-r 모드는 현재 폴더에 ./fast.log를 만들어 매번 빈것처럼 보임|cat ./fast.log로 확인|

### 배운점
suricata를 사용하여 IDS(침입탐지시스템)는 가능하지만 근본적인 원인을 막기엔 부족합니다. 
탐지만으로 끝내는 것이 아닌 방화벽으로 502번 포트를 차단해야 합니다.

---

## Github
https://github.com/simjungyu/OT-ICS-Security-Lab



