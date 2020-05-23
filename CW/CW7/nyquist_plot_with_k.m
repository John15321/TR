function [] = nyquist_plot_with_k(num, den, plot_name)
    fig = figure;
    nyquist(1 + (tf(num, den)), (-1 * tf(num, den)), (-3 * tf(num, den)))
    legend("k=1", "k=-1", "k=-3")
    print(fig, plot_name, '-dpng', '-r600')
    % close all;
    % fig2 = figure2;
    % pzmap(tf(num, den))
    % print(fig2, plot_name+"_pzmap", '-dpng','-r600')
    dlmwrite('./stabs.txt', [isstable(tf(num, den)), isstable(1 + tf(num, den))], 'delimiter', ',', '-append')
    clear all;
    close all;
end
