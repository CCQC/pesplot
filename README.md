# pesplot

Produces clean, publication quality plots of potential energy surfaces.

## Usage
See `example/input.dat` for an example input file.

### Input file syntax
```
$energies
<name1> <energy>
<name2> <energy>
...
$end
$connect
<name1> & <name2>
...
$end
$plot_format
<option_name> <option_val>
$end
```
### Options

| name | behavior |
|------|----------|
| `y_axis_top_extend` | Extend top of y axis this far beyond max energy |
| `y_axis_bot_extend` | Extend bottom of y axis this far beyond min energy | 
| `y_axis_label` | |
| `x_axis_right_extend` | |
| `x_axis_label` | |
| `name_vshift_scale` | |
| `name_font_size` | |
| `energy_vshift_scale` | |
| `energy_font_size` | |
| `species_line_spacing` | |
| `species_line_length` | |
| `species_line_width` | |
| `connection_line_width` | |
| `latex_text` | |
| `ytick_min` | |
| `ytick_min` | |
| `ytick_intvl | |
