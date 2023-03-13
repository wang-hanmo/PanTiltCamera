clear all;
clc
name = 'C:\Users\whm\Desktop\计算机系统设计\pan-tilt-camera\data\识别-大小.xlsx';
w = xlsread(name,'A2:A7');
d1 = xlsread(name,'B2:B7');
d2 = xlsread(name,'C2:C7');
f3 = line([0,35.727],[0,30],'color','b','linestyle',':');
hold on
f4 = line([0,800],[0,24.881],'color','r','linestyle','--');
hold on
f1 = plot(d1,w,'b*');
hold on
f2 = plot(d2,w,'ro');
axis([0 800 0 30]);
xlabel("物体距离(cm)");
ylabel("物体宽度(cm)");
legend([f1,f2,f3,f4],'实测最小距离','实测最大距离','理论最小距离','理论最大距离','Location','SouthEast');
grid;