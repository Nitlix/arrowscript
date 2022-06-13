import os


instructions = []
imports = []
with open('in.txt','r',encoding='utf-8') as e:
    instructions = e.readlines()



insidefunction = 0
space = '    '

with open('script.py','w+') as script:
    script.write('import discord\nimport math\nimport random\nimport json\nimport requests\nimport threading\nimport multiproccessing\nimport os\nimport sys')
    for x in instructions:
        if x.startswith('IF '):
            content = x.split(' ')
            content.remove('IF')
            if content[0] == 'EXISTS':
                if len(x[1].split(' ')) >= 2:
                    if x.endswith('{'):
                        
                        script.write(f"{space*insidefunction}files = os.listdir('.')\n{space*insidefunction}if '{str(x[1])}' in files:")
            
        if x.startswith('CREATE '):
            content = x.split(' ')
            content.remove('CREATE')
            if len(x[1].split(' ')) >= 2:
                script.write(f"{space*insidefunction}with open")
            
            if 