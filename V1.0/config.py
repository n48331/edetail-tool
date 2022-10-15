def createConfig(project_name, slide_names):
    # for name in slide_names:
    slides = ''
    s = ''
    for i in range(len(slide_names)):
        s += f'"s{str(i+1)}",'
        slides += f'''
        s{i+1}: {{
        name: "s{i+1}",
        zipFile: "{slide_names[i]}.zip",
        }},
        '''

    config = f'''var config = {{
        project: "{project_name}",
        slides: {{
        {slides}
        }},
        coreflow: {{
            /*First flow should have all the slides*/
            f0: {{
            content: [{s}],
            name: "Flow 0",
            }},
        
            }},

            }};

	'''
    f = open(f"config.js", "w+")
    f.write(config)
    f.close()
