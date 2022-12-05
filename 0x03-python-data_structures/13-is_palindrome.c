#include "lists.h"
#include <stdio.h>

listint_t *rev_listint(listint_t **head);
/**
  * rev_listint - Reverses a singly-linked listint_t list.
  * @head: pointer to starting node of list to be reversed
  *
  * Return: a pointer to the ehad of reversed list
  */
listint_t *rev_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}

/**
  * is_palindrome -  checks whether linked list is a palindrome
  * @head: head of linked list
  *
  * Return: 0 if not, 1 if it is
  */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rev = rev_listint(&tmp);
	mid = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	rev_listint(&mid);
	return (1);
}
