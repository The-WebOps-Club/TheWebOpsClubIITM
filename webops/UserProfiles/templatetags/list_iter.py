from django import template

register = template.Library()

@register.filter(name = 'list_iter')

def list_iter(lists):
	list_a, list_b, list_c = lists

	for x,y,z in zip(list_a, list_b, list_c):
		yield(x,y,z)

