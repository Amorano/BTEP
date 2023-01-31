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

race = ['asian', 'african', 'native american', 'european']
color = ['diamond', 'gold', 'platinum', 'emerald', 'ruby']

data = {
	'background': 'white',
	'species': 'human',
	'gender': 'male'
}

body = ""
for r in race:
	for c in color:
		body += pilot.format(race=r, color=c, **data) + '\n'

with open('__pilot.txt', 'w+', encoding='utf-8') as f:
	f.write(body)
