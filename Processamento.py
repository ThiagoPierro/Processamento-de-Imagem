from PIL import Image, ImageFilter


def open_image(file_path):
    """Abre uma imagem do caminho fornecido."""
    return Image.open(file_path)


def apply_filter(image, filter_type):
    """Aplica um filtro à imagem."""
    return image.filter(filter_type)


def save_image(image, output_path):
    """Salva a imagem processada no caminho especificado."""
    image.save(output_path)


if __name__ == "__main__":

    input_image_path = 'Leao.jpg'
    output_image_path = 'imagem_processada.jpg'


    imagem = open_image(input_image_path)


    imagem_pb = imagem.convert('L')


    imagem_processada = apply_filter(imagem_pb, ImageFilter.GaussianBlur(radius=2))


    imagem_processada.show()


    save_image(imagem_processada, output_image_path)

    print(f'Imagem processada salva como {output_image_path}')
