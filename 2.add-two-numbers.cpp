class Solution {
    public:
        void del(ListNode* l1) {
            if (l1->next)
                del(l1->next);
            delete l1;
        }
        ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
                ListNode carry(0);
            if (l1 != NULL && l2 != NULL) {
                int t = l1->val + l2->val;
                cout << t << endl;
                carry.val = t / 10;
                t %= 10;
                ListNode *r = new ListNode(t);
                r->next = addTwoNumbers(l1->next, l2->next);                                                                                                 
                if (carry.val)
                {
                    ListNode *t = r->next;
                    r->next = addTwoNumbers(&carry, t);
                    if (t)
                        del(t);
                }
                return r;
            }
            if (l1 != NULL)
                return addTwoNumbers(l1, &carry);
            if (l2 != NULL)
                return addTwoNumbers(l2, &carry);
                return NULL;
        }
};
