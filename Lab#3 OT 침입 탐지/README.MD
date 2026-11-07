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



