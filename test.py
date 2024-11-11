def separation_technique():
    print("Welcome to the Advanced Separation Technique Finder!\n")

    answer1 = input("Is the mixture a solid-liquid, liquid-liquid, gas mixture, or solid-solid? (solid-liquid/liquid-liquid/gas/solid-solid): ").strip().lower()

    if answer1 == 'solid-liquid':
        answer2 = input("Is the solid dissolved in the liquid? (yes/no): ").strip().lower()
        if answer2 == 'yes':
            answer3 = input("Do you want to purify the dissolved solid? (yes/no): ").strip().lower()
            if answer3 == 'yes':
                answer4 = input("Are there impurities that need to be removed? (yes/no): ").strip().lower()
                if answer4 == 'yes':
                    print("\nYou can use **Recrystallization**.")
                else:
                    print("\nYou can use **Crystallization**.")
            else:
                print("\nYou can use **Crystallization**.")
        else:
            answer5 = input("Are the solid particle size significantly larger than the liquid? (yes/no): ").strip().lower()
            if answer5 == 'yes':
                print("\nYou can use **Filtration**.")
            else:
                answer6 = input("Is the liquid viscous? (yes/no): ").strip().lower()
                if answer6 == 'yes':
                    print("\nYou can use **Decantation** or **Centrifugation**.")
                else:
                    print("\nYou can use **Decantation** or **Filtration** depending on the situation.")

    elif answer1 == 'liquid-liquid':
        answer7 = input("Are the liquids miscible? (yes/no): ").strip().lower()
        if answer7 == 'no':
            print("\nYou can use **Liquid-Liquid Extraction**.")
        else:
            answer8 = input("Do the liquids have significantly different boiling points? (yes/no): ").strip().lower()
            if answer8 == 'yes':
                answer9 = input("Is the boiling point difference greater than 25°C? (yes/no): ").strip().lower()
                if answer9 == 'yes':
                    print("\nYou can use **Simple Distillation**.")
                else:
                    print("\nYou can use **Fractional Distillation**.")
            else:
                answer10 = input("Are the liquids colored? (yes/no): ").strip().lower()
                if answer10 == 'yes':
                    print("\nYou can use **Chromatography**.")
                else:
                    print("\nYou can use **Fractional Distillation**.")

    elif answer1 == 'gas':
        answer11 = input("Is the gas mixture a vapour or a gas? (vapor/gas): ").strip().lower()
        if answer11 == 'vapour':
            answer12 = input("Are the components chemically similar? (yes/no): ").strip().lower()
            if answer12 == 'yes':
                print("\nYou can use **Fractional Distillation**.")
            else:
                print("\nYou can use **Adsorption** techniques.")
        else:
            answer13 = input("Are the gases reactive? (yes/no): ").strip().lower()
            if answer13 == 'yes':
                print("\nYou can use **Chemical Absorption**.")
            else:
                print("\nYou can use **Gas Chromatography**.")

    elif answer1 == 'solid-solid':
        answer14 = input("Are the solids different in size or density? (yes/no): ").strip().lower()
        if answer14 == 'yes':
            print("\nYou can use **Sieving** or **Flotation**.")
        else:
            answer15 = input("Do the solids have different magnetic properties? (yes/no): ").strip().lower()
            if answer15 == 'yes':
                print("\nYou can use **Magnetic Separation**.")
            else:
                answer16 = input("Is one of the solids soluble in a suitable solvent while the other is not? (yes/no): ").strip().lower()
                if answer16 == 'yes':
                    print("\nYou can use **Differential Dissolution**.")
                else:
                    print("\nYou can use **Handpicking** depending on the situation.")

    else:
        print("\nNo suitable separation technique found for the given mixture.")

separation_technique()
