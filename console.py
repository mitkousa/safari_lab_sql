import pdb 
from models.staff import Staff
import repositories.staff_repository as staff_repo  

# staff_repo.delete_all()

staff1 = Staff('Nigel Thornberry', '01-09-1998', 'Big cats', 3)
staff_repo.save(staff1)

staff2 = Staff('Eliza Thornberry', '30-12-2011', 'Aviary', 4)
staff_repo.save(staff2)

# staff_repo.select_all()

pdb.set_trace()