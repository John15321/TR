function [] = nyquist_plot_with_k(num, den, plot_name)
    fig = figure;
    nyquist(1 + (tf(num, den)), 1 + (2 * tf(num, den)), 1 + (3 * tf(num, den)))
    legend("k=1", "k=2", "k=3")
    print(fig, plot_name, '-dpng', '-r600')
    dlmwrite('./stabs.txt', [isstable(tf(num, den)), isstable(1 + tf(num, den))], 'delimiter', ',', '-append')
    clear all;
    close all;
end
