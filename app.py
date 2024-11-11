from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    image_path = "" 
    image_path2 = ""
    image_path3 = ""  
    image_path4 = ""
    if request.method == 'POST':
        answers = request.form
        mixture_type = answers.get('mixture_type')

        if mixture_type == 'solid-liquid':
            if answers.get('dissolved') == 'yes':
                if answers.get('purify') == 'yes':
                    if answers.get('impurities') == 'yes':
                        result = "You can use Distillation."
                        image_path3 = "static/Distillation_png"
                    else:
                        result = "You can use Crystallization."
                        image_path3 = "static/Crystallization_.png"
                else:
                    result = "You can use Crystallization."
                    image_path3 = "static/Crystillzation_.png"
            else:
                if answers.get('particle_size') == 'yes':
                    result = "You can use Filtration."
                    image_path3 = "static/Filtration_.png"
                else:
                    if answers.get('viscous') == 'yes':
                        result = "You can use Decantation or Centrifugation."
                        image_path3 = "static/Centrifugation_.png"
                        image_path4 = "static/Decantation_.png"
                    else:
                        result = "You can use Decantation or Filtration."
                        image_path3 = "static/Decantation_.png"
                        image_path4 = "static/Filtration.png"

        elif mixture_type == 'liquid-liquid':
            if answers.get('miscible') == 'no':
                result = "You can use Decantation."
                image_path3 = "static/Decantation_.png"
            else:
                if answers.get('boiling_difference') == 'yes':
                    if answers.get('greater_than_25') == 'yes':
                        result = "You can use Simple Distillation."
                        image_path3 = "static/Distillation_.png"
                    else:
                        result = "You can use Fractional Distillation."
                        image_path3 = "static/Fractional Distillation_.png"
                else:
                    if answers.get('colored') == 'yes':
                        result = "You can use Chromatography."
                        image_path3 = "static/Chromatography_.png"
                    else:
                        result = "You can use Fractional Distillation."
                        image_path3 = "static/Fractional Distillation_.png"

        elif mixture_type == 'gas-gas':
            if answers.get('vapor_or_gas') == 'vapor':
                if answers.get('chemically_similar') == 'vapor':
                    result = "You can use Fractional Distillation."
                    image_path3 = "static/Fractional Distillation_.png"
                else:
                    result = "You can use Adsorption."
                    image_path3 = "static/Adsorption_.png"
            else:
                if answers.get('reactive') == 'yes':
                    result = "You can use Adsorption."
                    image_path3 = "static/Adsorption_.png"
                else:
                    result = "You can use Cryogenic Distillation"
                    image_path3 = "static/Cryogenic Distillation_.png"

        elif mixture_type == 'solid-solid':
            if answers.get('different_size_density') == 'yes':
                result = "You can use Sieving if the size is different and Centrifugation if the density is different."
                
                image_path3 = "static/Centrifugation_.png"
                image_path4 = "static/Sieving_.png"
            else:
                if answers.get('magnetic_properties') == 'yes':
                    result = "You can use Magnetic Separation."
                    image_path3 = "Magnetic Sepration_.png"
                else:
                    if answers.get('soluble') == 'yes':
                        result = "You can use Dissolution followed by filtration or crystillzation."
                        image_path3 = "Dissolution_.png"

                    else:
                        result = "You can use Handpicking depending on the situation."
                        image_path = "static/Handpicking.png"

        else:
            result = "Select a mixture type"

    return render_template('index.html', result=result, image_path=image_path, image_path2=image_path2, image_path3=image_path3, image_path4=image_path4)

if __name__ == '__main__':
    app.run(debug=True)

