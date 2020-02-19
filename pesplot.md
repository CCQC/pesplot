# Using pesplot

## TL;DR

Pull a fresh version of pesplot from github:
`git clone https://github.com/CCQC/pesplot`

In that directory, go to the "example" directory. There is a file (input.dat) that looks like this:

```
$energies
MVR_O2  0.0
PR      -21.60
TS1     -1.1
QR1     -20.0
TS7     -10.4
HPECO   -15.2
P1      -48.9
test    -30.0 above PR
test1   -35.0 above TS1
test1a  -5.0 above TS1
test2   -25.0 above HPECO
$end


$connect
MVR_O2  - PR
PR      & TS1
TS1     <- QR1
QR1     -> TS7
TS7     -- HPECO
MVR_O2  - test
PR      : test1
PR      > test1a
test1a  < TS7
TS7     <--> test2
$end

$plot_format
energy_precision = 1 #Num. of decimal places in energies
ytick_min = -50.0
ytick_max =  5.0
ytick_intvl = 5.0
$end
```

The `$energies` section is split into two parts; first is one species for each column you wouldl like to have.
Second, place species you want stacked with `<name> <energy> above <name2>` to place it above (or below) another species (`<name2>`)
In previous versions, species were numbered and referenced by number in the "above" syntax. This is not the case anymore. 

The `$connect` section is formatted like:
```
<name1> <marker> <name2>
```
This connects `<name1>` and `<name2>` with a dashed black line. You can use any of the markers shown in the example, if you prefer.

## Editing the PDF
Use the program `inkscape` to edit the pdf. You can move objects around, change their color, and so forth.
