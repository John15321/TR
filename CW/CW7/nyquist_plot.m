function [] = nyquist_plot(num, den, plot_name)
    fig = figure;
    nyquist(tf(num, den))
    print(fig, plot_name, '-dpng','-r600')
    % close all;
    % fig2 = figure2;
    % pzmap(tf(num, den))
    % print(fig2, plot_name+"_pzmap", '-dpng','-r600')
    dlmwrite('./stabs.txt', [isstable(tf(num, den)), isstable(1+tf(num, den))], 'delimiter', ',', '-append')
    clear all;
    close all;
end
