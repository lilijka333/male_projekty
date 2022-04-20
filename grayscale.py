from argparse import ArgumentParser
from glob import glob
from PIL import Image, ImageFilter


parser = ArgumentParser(description='Zamiana jpgów na czarno-białe')
parser.add_argument('--input', help='Folder z którego pobieram obrazki', required=True)
parser.add_argument('--output', help='Folder do którego zapisze obrazki', required=True)
args = parser.parse_args()
print(args.input, args.output)


for path in glob(args.input + '/*'):
    directory, filename = path.split('\\')
    print(path, directory, filename)

    with Image.open(path) as new_image:
        grayscale_image = new_image.convert('L')
        modified_image = grayscale_image.filter(ImageFilter.DETAIL)
        modified_image.save(args.output + '/modified' + filename)
