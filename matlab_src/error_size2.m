clear all;
clc
name = 'C:\Users\whm\Desktop\计算机系统设计\pan-tilt-camera\data\误差-大小.xlsx';
x1 = xlsread(name,'N2:N10');
y1 = xlsread(name,'O2:O10');
x2 = xlsread(name,'P2:P10');
y2 = xlsread(name,'Q2:Q10');
x3 = xlsread(name,'R2:R9');
y3 = xlsread(name,'S2:S9');
f1 = plot(x1,y1,'-dr');
hold on 
f2 = plot(x2,y2,'-*g');
hold on 
f3 = plot(x3,y3,'-xb');
hold on 
axis([0 30 0 0.2])
xlabel('物体宽度(cm)')
ylabel('误差%')
legend([f1,f2,f3],'物体距离=100cm','物体距离=150cm','物体距离=200cm');