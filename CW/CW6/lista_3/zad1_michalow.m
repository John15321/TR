close all;
clear all;



w=0:0.1:4.5;


M=w.^4-17*(w.^2)+6+(-7*(w.^3)+17*w)*i;
figure(1)
grid on
hold on


plot(M);

title("a) M(wj)=w^{4}-17w^{2}+6+(-7w^{3}+17w)i");
xlabel("Re");
ylabel("Im");

w=0:0.1:4;


M=(w*i).^4+6*(w*i).^3+13*(w*i).^2+12*w*i+4;
figure(2)
grid on
hold on


plot(M);

title("b) M(wj)=(wi)^{4}+6(wi)^{3}+13(wi)^{2}+12wi+4");
xlabel("Re");
ylabel("Im");


w=0:0.1:4;

M=(w*i).^3+4*(w*i).^2+w*i-6;
figure(3)
grid on
hold on


plot(M);

title("c) M(wj)=(wi)^{3}+4(wi)^{2}+wi-6");
xlabel("Re");
ylabel("Im");



w=0:0.1:4;

M=(w*i).^3+6*(w*i).^2+11*w*i+6;
figure(4)
grid on
hold on


plot(M);

title("d) M(wj)=(wi)^{3}+6(wi)^{2}+11wi+6");
xlabel("Re");
ylabel("Im");