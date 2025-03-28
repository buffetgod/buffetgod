### 场效应管

- 场效应晶体管（Field Effect Transistor缩写(FET)）简称场效应管。
- 场效应管属于电压控制型半导体器件。具有输入电阻高、噪声小、功耗低、动态范围大、易于集成、没有二次击穿现象、安全工作区域宽等优点。

### MOS管分类

- 按沟道分类，场效应管分为PMOS管（P沟道型）和NMOS（N沟道型）管。
> ![image](https://github.com/user-attachments/assets/d583518e-b2a2-4f37-990c-e887bcd73129)
- 按材料分类，可以分为分为耗尽型和增强型：
> 说明：**增强型管**：栅极-源极电压 Vgs 为零时漏极电流也为零；**耗尽型管**：栅极-源极电压 Vgs 为零时漏极电流不为零。在实际应用中，以 增强型NMOS 和 增强型PMOS 为主。                        
> ![image](https://github.com/user-attachments/assets/5aea5b56-9649-4ca9-b900-84d9bf5ac853)

### MOS管输出特性曲线

- MOS管的输出特性可以分为三个区：夹断区(截止区)、恒流区、可变电阻区。
> ![image](https://github.com/user-attachments/assets/c4aab15b-0d4d-44c6-936c-7fe2bd11b3c6)
- **夹断区**(截止区)：VGS < VGS(th)时，表示MOS管不能导电，处在截止状态。电流ID为0，管子不工作。
- **恒流区**：VGS≥VGS(th)，且VDS>VGS-VGS(th)，电流ID基本不随VDS变化，ID的大小主要决定于电压VGS，所以叫做恒流区，也叫饱和区
- **可变电阻区**：VGS>VGS(th) ，且VDS < VGS - VGS(th),Id随着Vds的增加而上升，两者基本上是线性关系，所以可以看作是一个线性电阻，当VGS不同电阻的阻值就会不同，所以在该区MOS管相当就是一个由VGS控制的可变电阻。
- **击穿区**: 随着VDS增大，PN结承受太大的反向电压而被击穿。

### MOS管参数

![image](https://github.com/user-attachments/assets/b7055d94-d997-43c1-8834-d497d71261b4)
- VGS(th)(开启电压)
- VGS(最大栅源电压)
> 说明：栅极能够承受的最大电压，栅极是MOS管最薄弱的地方，设计的时候得注意一下，加载栅极的电压不能超过这个最大电压。
- RDS(on)(漏源电阻)、
> 说明：导通时漏源间的最大阻抗，它决定了MOSFET导通时的消耗功率。
- ID(导通电流)
- VDSS(漏源击穿电压)
> 说明：漏源击穿电压是指栅源电压VGS 为 0 时，场效应管正常工作所能承受的最大漏源电压。

### MOS管的封装

- SOT-23
  > ![image](https://github.com/user-attachments/assets/f4d6bd7a-7005-48a0-853c-803d7a959eef)
- SOT-223
  > ![image](https://github.com/user-attachments/assets/51f5bcfa-ef5b-49c9-8754-b70f899bc855)
- TO-252(大功率)
  > ![image](https://github.com/user-attachments/assets/5f95d934-c045-4627-9b5e-b192175a9d42)
- TO-220/220F(大功率)
  >  ![image](https://github.com/user-attachments/assets/dd9dff89-f6ca-43f9-9872-558377508fde)

### MOS管判别

- 判别是NMOS 还是 PMOS 以及MOS管好坏。将万用表调至二极管档，将红表笔接在MOS的S极，黑表笔接在D极，如果这时候万用表显示0.4V~0.9V（二极管特性，不同MOS管有一定差异）电压值，说明这很可能是一个 NMOS；如果没有读数，说明这很可能是一个PMOS。

### MOS管应用
- 开关电路
- 电平转换
  > ![image](https://github.com/user-attachments/assets/0db2b918-72b6-4a6c-b89a-13f0f1ffc4e8)
  > 
  > 注意事项：
  > - 该电路不能用于推挽输出的IO口，只能用于收发双方都是开集（Open Collector, OC）或开漏（Open Drain, OD）结构输出的双向信号线。比如常见的I2C通讯。
  > - VCC_S1 <= VCC_S2 (mos管自带二极管)
  > - MOS管导通电压门限（Vth(GS)里面的最大值）需要小于低电源电压。






























### [转载](https://bbs.huaweicloud.com/blogs/375339)
