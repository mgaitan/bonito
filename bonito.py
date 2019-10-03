#!/usr/bin/env python3
"""
Bonito

Usage:
  bonito <svg> [--desde=<desde>] [--hasta=<hasta>] [--grupos=<grupos>] [--planchas=<planchas>] [--marca=<marca>] [--repe=<repe>]
  bonito -h | --help
  bonito --version

Options:
  -h --help           Show this screen.
  --version           Show version.
  --desde=<desde>     Primer número [default: 0].
  --hasta=<hasta>     Último número [default: 100].
  --grupos=<hasta>    Tamaño talonario [default: 10].
  --planchas=<hasta>  Repetir talon [default: 1].
  --marca=<marca>     Marca a reemplaza [default: XXX]
  --repe=<repe>       Incrementar cada [default: 2]  
"""


from docopt import docopt
import sys, os
import subprocess
from pathlib import Path
import glob


def mark_to_num(content, num, mark, repe):
    num_as_string = f'{num:0{len(mark)}}'
    return content.replace(mark, num_as_string, repe)


def main():
    arguments = docopt(__doc__, version='0.2')
    
    desde = int(arguments['--desde'])
    hasta = int(arguments['--hasta'])
    repe = int(arguments['--repe'])
    marca = arguments['--marca']
    svg_path = Path(arguments['<svg>'])
    svg_content = svg_path.read_text()
    number_by_page = int(svg_content.count(marca) / repe)
    grouped_by =  int(arguments['--grupos'])
    planchas =  int(arguments['--planchas'])
        

    for plancha in range(planchas):
        counter_from = desde + plancha * number_by_page * grouped_by


        for pagina in range(grouped_by):
            page_content = svg_content
            for bono in range(number_by_page):
                num_remplazo = counter_from + bono * grouped_by + pagina
                page_content = mark_to_num(page_content, num_remplazo, mark=marca, repe=repe)

            with open('temp.svg', 'w') as output_svg:
                output_svg.write(page_content)

            # convert pagina to pdf
            subprocess.call(["inkscape", "-f", 'temp.svg', '--export-dpi=150', '-A', f'temp{pagina:04}.pdf'])

        # join 
        generator = ['gs',
                     '-q',
                     '-sPAPERSIZE=a4',
                     '-dNOPAUSE',
                     '-dBATCH',
                     '-sDEVICE=pdfwrite',
                     f'-sOutputFile={svg_path.stem}-{counter_from:0{len(marca)}}-{num_remplazo:0{len(marca)}}.pdf'] + \
                     [f'temp{pagina:04}.pdf' for pagina in range(grouped_by)]

        subprocess.call(generator)

        for temp in glob.glob('temp*'):
            os.remove(temp)


if __name__ == '__main__':
    main()