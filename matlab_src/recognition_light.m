clear all;
clc
name = 'C:\Users\whm\Desktop\计算机系统设计\pan-tilt-camera\data\识别-光照.xlsx';
y1 = xlsread(name,'B2:B36');
x1 = xlsread(name,'C2:C36');
y2 = xlsread(name,'E2:E36');
x2 = xlsread(name,'F2:F36');

f1 = plot(x1,y1,'r*');
hold on
f2 = plot(x2,y2,'b+');
line([0,210],[45,255],'color','m','linewidth',2);
line([0,255],[0,255],'color','k','linestyle','--');
axis([0 255 0 255]);
xlabel("物体灰度值");
ylabel("背景灰度值");
legend([f1,f2],'Recognized','Unrecognized','Location','SouthEast');
grid;