clear all;
clc
name = 'C:\Users\whm\Desktop\计算机系统设计\pan-tilt-camera\data\误差-大小.xlsx';
x = xlsread(name,'A2:A122');
y = xlsread(name,'B2:B122');
z = xlsread(name,'D2:D122');
xn = linspace(0,34,35);
yn = linspace(0,549,550);
[Xn,Yn] = meshgrid(xn,yn);
Zn = griddata(x,y,z,Xn,Yn,'cubic');
surf(Xn,Yn,Zn);
shading interp
%mesh(Xn,Yn,Zn)
axis([0 35 0 600 0 0.2])
xlabel('物体宽度(cm)')
ylabel('物体距离(cm)')
zlabel('误差%')
hold on
plot3(x,y,z,'r+')