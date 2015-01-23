--hw3.hs
--Nicolas Hahn


--keys = k
--values = v
data BST k v = Empty |
               Node k v (BST k v) (BST k v)

val :: BST k v -> Maybe v
val k v = if 