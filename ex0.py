formatter = "%r %r %r %r"

print formatter % (1, 2 , 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	#Python displays double quotes for strings that has a single quote in it (vs. single quotes for any other string)
	"But it didn't sing.",
	"So I said goodnight."
	)