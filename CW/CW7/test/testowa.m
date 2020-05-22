function [] = testowa(num, den, plot_name)
nyquist(tf(num, den))
grid on
saveas(gcf, plot_name)
end

