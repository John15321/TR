
num = [1]
den = [1 2 1]

nyquist(tf(num, den), 2*tf(num, den), 3*tf(num, den))
legend("TWOJA", "STARA", "JEBANA")
%saveas(gcf, plot_name)
%dlmwrite('./stabs.txt',isstable(tf(num, den)),'delimiter',',','-append')