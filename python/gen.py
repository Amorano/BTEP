"""The base prompts to generate the core image types.

DPM++ SDE Karras, 10s, 18g, 0.8d

vector logo for eagle, transparent background, symmetrical, three colors, flat shading, by Ed Mell
vector logo for skull, transparent background, symmetrical, three colors, flat shading, by Ed Mell
vector logo for tank, transparent background, symmetrical, three colors, flat shading, by Ed Mell
vector logo for planet, transparent background, symmetrical, three colors, flat shading, by Ed Mell
vector logo for mountain, transparent background, symmetrical, three colors, flat shading, by Ed Mell
vector logo for tower, transparent background, symmetrical, three colors, flat shading, by Ed Mell
"""

pilot = "mdjrny-v4 style full head shot portrait of {species} {race} {gender} battletech commander in futuristic {color} uniform on a {background} background, looking at viewer, symmetry, Esad Ribic, Adam Hughes, light shades of {color}, Lee Bermejo, no text, no logo, no number, space, gundam, mech"
pilot = "mdjrny-v4 style full head shot portrait of {species} {race} {gender} battletech commander in futuristic {color} uniform on a {background} background, no helmet, looking at viewer, symmetry, Esad Ribic, Adam Hughes, light shades of {color}, Lee Bermejo, no text, no logo, no number"

pilot = "1/4 body full head shot portrait of {species} {race} {gender} battletech mech commander in intricate futuristic {color} uniform on a {background} background, looking at viewer, symmetry, Esad Ribic, Adam Hughes, light shades of {color}, Lee Bermejo"

race = ['asian', 'african', 'native american', 'european']
color = ['diamond', 'gold', 'platinum', 'emerald', 'ruby']

data = {
	'background': 'neutral gray, geometric',
	'species': 'human',
	'gender': 'female',
	'race': 'blonde',
}

body = ""
for r in race:
	for c in color:
		body += pilot.format(color=c, **data) + '\n'

with open('__gen.txt', 'w+', encoding='utf-8') as f:
	f.write(body)
