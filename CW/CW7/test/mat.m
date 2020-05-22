sys = tf([1], [1 2 3 4])
nyquist(sys)
grid on
saveas(gcf, "testoweplot.png")