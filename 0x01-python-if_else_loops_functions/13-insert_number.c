#include "lists.h"
/**
  * insert_node - inserts number into sorted singly linked list
  * @head: head of sorted list
  * @number: number to insert
  *
  * Return: address of the new node
  */
listint_t *insert_node(listint_t **head, int number)
{ /* pointers to listint_t lists */
	listint_t *curr = NULL, *nn = NULL, *temp = NULL;
	/* allocate space for new node */
	nn = malloc(sizeof(listint_t));
	if (nn == NULL) /* malloc failure */
		return (NULL);
	nn->n = number; /* new node points to number */
	if (*head)
	{	/* current points to a pointer to head of linked list */
		curr = *head;
		/* if number is less than or equal to current node */
		if (number <= curr->n)
		{ /* make new node point to current list */
			nn->next = curr;
			*head = nn; /* pointer to head now equals new node */
		}
		else
		{
			while (curr->next)
			{	/* if number less than or equal to current's next next node */
				if (number <= curr->next->n)
				{ /* insert number */
					temp = curr->next;
					curr->next = nn;
					nn->next = temp;
					return (*head);
				}
				/* travers to next node */
				curr = curr->next;
			}
			/* insert number */
			temp = curr->next;
			curr->next =nn;
			nn->next = temp;
		}
		return (*head);
	}
	/* terminate new node */
	nn->next = NULL;
	*head = nn; /* pointer to head is now the new node */
	return (*head);
}
