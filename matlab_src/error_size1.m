clear all;
clc
name = 'C:\Users\whm\Desktop\计算机系统设计\pan-tilt-camera\data\误差-大小.xlsx';
x0 = xlsread(name,'A2:A51');
y0 = xlsread(name,'G2:G51');
x1 = xlsread(name,'A52:A101');
y1 = xlsread(name,'G52:G101');
x2 = xlsread(name,'A102:A151');
y2 = xlsread(name,'G102:G151');
x3 = xlsread(name,'A152:A201');
y3 = xlsread(name,'G152:G201');
x4 = xlsread(name,'A202:A251');
y4 = xlsread(name,'G202:G251');
x5 = xlsread(name,'A252:A301');
y5 = xlsread(name,'G252:G301');
plot(x0,y0,'-or');
hold on
plot(x1,y1,'-+g');
hold on
plot(x2,y2,'-*b');
hold on
plot(x3,y3,'-dy');
hold on
plot(x4,y4,'-xm');
hold on
plot(x5,y5,'-sc');
hold on
axis([0 450 0 0.12])
xlabel('距离D(cm)')
ylabel('误差error')
legend("E=8lux","E=706lux","E=1404lux","E=2102lux","E=2800lux","E=3498lux");