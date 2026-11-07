# OT/ICS Security Lab

OT/ICS 보안 구축 실습 기록

OT Security | Network Segmentation | Modbus | IDS

2026-11-06

---

## Lab 01 - OT/IT 망 분리 구축

### 구성 토폴로지

<img width="386" height="289" alt="image" src="https://github.com/user-attachments/assets/6c4288a1-d023-4c94-bafc-db2e1c7e4040" />

| 구분 | Network | VLAN | Gateway |
| --- | --- | --- | --- |
| OT Network | 192.168.10.0/24 | VLAN 10 | 192.168.10.1 |
| IT Network | 10.0.0.0/24 | VLAN 20 | 10.0.0.1 |

### Config

```cisco
hostname OT-Core-SW
vlan 10
 name OT
vlan 20
 name IT

interface vlan 10
 ip address 192.168.10.1 255.255.255.0
 no shutdown

interface vlan 20
 ip address 10.0.0.1 255.255.255.0
 no shutdown

interface f0/10
 switchport mode access
 switchport access vlan 10
 no shutdown

interface f0/20
 switchport mode access
 switchport access vlan 20
 no shutdown

ip routing
```

### 통신 테스트

<img width="636" height="509" alt="image" src="https://github.com/user-attachments/assets/5fc665b5-2b38-4d62-b97e-1089c6b36a1e" />


- OT-PC1에서 Gateway 192.168.10.1로 Ping 성공
- VLAN 간 L3 통신 확인

### 트러블슈팅

| 문제 | 원인 | 해결 |
| --- | --- | --- |
| 인터페이스 활성화가 되지 않음 | PC와 스위치에 Cross 케이블 사용 | Cross에서 Direct 케이블로 교체 |

### 배운 점

실무에서는 OT망과 IT망 사이에 DMZ를 두고 OPC-UA Gateway를 통해서 데이터를 전달합니다.
이번 실습에서는 그 첫 단계인 L3 분리를 구현한 것이며, 다음 실습에서는 ACL로 OT망 인터넷 차단을 추가해 볼 예정입니다.

---

## Github

https://github.com/ji3353836-web/OT-ICS-Security-Lab
