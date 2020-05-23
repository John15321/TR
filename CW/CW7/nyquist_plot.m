function [] = nyquist_plot(num, den, plot_name)
    fig = figure;
    nyquist(1 + tf(num, den))
    print(fig, plot_name, '-dpng','-r600')
    dlmwrite('./stabs.txt', [isstable(tf(num, den)), isstable(1+tf(num, den))], 'delimiter', ',', '-append')
    clear all;
    close all;
end
