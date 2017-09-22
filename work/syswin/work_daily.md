
2017/9/21
工作日报：
----------
CLOUD2.0
Ocata版中创建虚机支持VIP, 相关代码测试并提交：
1. 修改`prevent_arp_spoofing`默认值为`false`
2. 在 security group 中新增配置`prevent_iptables_ip_spoofing`，默认值为`false`。
3. 在`_add_fixed_egress_rules` 中添加配置项 `check `prevent_iptables_ip_spoofing`

CMDB2.0
1. 基于原型图整理用例图，工作分解；
2. DEV环境解决解决请求404的问题；

2017/9/22
工作日报：
----------
CMDB2.0
1. CMDB2.0 功能测试，模拟数据录入，功能演示,；

MPC
1. MPC生产环境(门头沟环境)代码更新；
