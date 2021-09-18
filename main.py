CHARACTERS = [
	'chleba',
	'rohlík',
	'houska',
	'dalamánek',
	'vánočka',
	'děda'
]

CHARACTER_VERSIONS = [
	'{character}',
	'{character} s máslem',
	'{character} s máslem se salámem',
]


# a list to aggregate all members to
# the story's "group"
all_characters = []

# for every character, we generate
# all of its versions
for character in CHARACTERS:
	for version in CHARACTER_VERSIONS:
		all_characters.append(version.format(character=character))

# the story's "group"
group = []

# for all members
for i in range(len(all_characters)-1):
	
	# transfer the first member
	# to be collected to our group
	group.append(all_characters.pop(0))

	# story wise, we treat all_characters[0]
	# as the next character to join
	# our group
	print('Takže jde {group} a potká {new_character}. A {new_character} povidá "{group} můžu jít s váma?", přičemž {group} odpoví "jo můžeš".'.format(
		group=', '.join(group),
		new_character=all_characters[0]
	))
