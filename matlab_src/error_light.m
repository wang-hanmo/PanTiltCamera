clear all;
clc
name = 'C:\Users\whm\Desktop\计算机系统设计\pan-tilt-camera\data\误差-光照.xlsx';
x0 = xlsread(name,'B2:B51');
y0 = xlsread(name,'G2:G51');
x1 = xlsread(name,'B52:B101');
y1 = xlsread(name,'G52:G101');
x2 = xlsread(name,'B102:B151');
y2 = xlsread(name,'G102:G151');
x3 = xlsread(name,'B152:B201');
y3 = xlsread(name,'G152:G201');
x4 = xlsread(name,'B202:B251');
y4 = xlsread(name,'G202:G251');
x5 = xlsread(name,'B252:B301');
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
axis([0 3500 0 0.12]);
xlabel("照度E(lux)");
ylabel("误差error");
grid;
legend("D=20cm","D=106cm","D=192cm","D=278cm","D=364cm","D=450cm");