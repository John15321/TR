clear
clc
close all
nom = [1];
den = [ 1, 1, 0 ];
K = tf(nom, den)
ilaplace(tf(nom, den))