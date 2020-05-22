function [] = nyquist_plot_with_k(num, den, plot_name)
nyquist(tf(num, den))
saveas(gcf, plot_name)
dlmwrite('./stabs.txt',isstable(tf(num, den)),'delimiter',',','-append')
end