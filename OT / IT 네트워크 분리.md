# OT-ICS-Security-Lab

> OT/ICS 보안 구축 실습 기록**  
> `Smart Factory OT Security | Network Segmentation | Modbus | IDS`

---

### 사용 기술
- **Network:** Cisco Packet Tracer (2960, 3560), VLAN, L3 Switching, ACL
- **OT Protocol:** Modbus TCP, OpenPLC
- **Security:** Wireshark, Suricata IDS, Fail2Ban
- **OS:** Rocky Linux, Kali Linux

## 실습 01: OT/IT 네트워크 분리

### 구성 토폴로지
<img width="386" height="289" alt="토폴로지" src="https://github.com/user-attachments/assets/81c83eac-0c5d-4859-82c6-43d621c15f03" />

- **OT Network:** 192.168.10.0/24 | VLAN 10 | GW: 192.168.10.1
- **IT Network:** 10.0.0.0/24 | VLAN 20 | GW: 10.0.0.1

### Config

<details>
<summary>OT-Core-SW 3560 Config 보기</summary>

```cisco
hostname OT-Core-SW
vlan 10
 name OT
vlan 20
 name IT

int vlan 10
 ip add 192.168.10.1 255.255.255.0
 n sh

int vlan 20
 ip add 10.0.0.1 255.255.255.0
 n sh

int f0/10
 sw m acc
 sw acc vlan 10

int f0/20
 sw m access
 sw m ac vlan 20

ip routing
```

</details>

### 통신 테스트

<img width="636" height="509" alt="OT-PC1핑성공" src="https://github.com/user-attachments/assets/521fb637-c1f6-47da-a6be-d65852f508b2" />

### 트러블슈팅

| 문제 | 원인 | 해결 |
| :--- | :--- | :--- |
| 인터페이스 활성화가 되지 않음 | pc와 스위치는 **Direct**케이블을 사용함 | **Cross**에서**Direct**케이블로 교체 |

### OT Insight

> 실무에서는 OT망과 IT망 사이에 DMZ를 두고 OPC-UA Gateway를 통해서 데이터를 전달합니다.  
> 이번 실습은 그 첫 단계인 **L3 분리**를 구현한 것이며 다음 실습에서는 **ACL로 OT망 인터넷 차단**을 추가해 볼 예정입니다.

---

### 연락처
Email : sim20910@naver.com
