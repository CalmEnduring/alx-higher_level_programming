#include "lists.h"
/**
  * check_cycle - checks if a singly linked list has a cycle
  * @list: linked list
  *
  * Return: 0 if there is no cycle, 1 if there is a cycle
  */
int check_cycle(listint_t *list)
{
	/* pointers to listint_t list */
	listint_t *current, *runner;
	/* if node or list is NULL, there is no cycle */
	if (list == NULL || list->next == NULL)
		return (0);

	current = list->next; /* next node */
	runner = list->next->next; /* node after the next node */
	/* traverse the linked list */
	while (current && runner && runner->next)
	{ /* if both runner + current ends in same place, cycle exists */
		if (current == runner)
			return (1);

		current = current->next; /* onto the next node */
		runner = runner->next->next; /* onto the node after next */
	}
	return (0);
}
