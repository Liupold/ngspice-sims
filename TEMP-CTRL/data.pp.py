from rohnch.prac_tools import *

R1 = 10
Vp = 12
Vn = -12

dt1 =  DT(("Temp", "Voltage"), [
        30,3.73,
        30.5,3.5,
        31.5,3.37,
        33.5,3.21,
        35,3.1,
        36.5,2.96,
        39,2.87,
        40.5,2.77,
        43,2.65,
        45,2.62,
        51,2.49,
        51,2.33,
        55,2.25,
        58,2.09,
        59.5,2.05,
        65,1.94,
        67,1.81,
        68.5,1.76,
        69.5,1.74,
        70,1.7,

])


dt2 = DT( ("Temp", "Voltage"), [
    75,1.89,
    70,2.07,
    65, 2.28,
    60, 2.49
])


dt1.to_csv('inc.csv')
dt2.to_csv('dec.csv')

fit1, _ = FIT(
        eqn = lambda x, m, c:  m*x + c,
        x = dt1.Temp,
        y = dt1.Voltage,
)

fit2, _ = FIT(
        eqn = lambda x, m, c: m*x + c, #  y = m*x + c
        x = dt2.Temp,
        y = dt2.Voltage,
)

print(fit2())
print(sum((fit2(dt2.Temp) - dt2.Voltage)**2))
PLOT("plot.pdf",
        title='calibration graph',
        xlabel = 'Tempertature in ($^{\circ}C$)',
        ylabel = 'Voltage difference across TS in (V)',
        inc = [dt1.Temp, dt1.Voltage, "o"],
        fit_inc =  [fit1, (30, 80, 1000), "-"],
        dec = [dt2.Temp, dt2.Voltage, "o"],
        fit_dec = [fit2, (30, 80, 1000), "-"],
)
