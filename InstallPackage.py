"""
Order of software packages to be built based on their dependencies

Given a graph showing the dependencies, find the install order

"""

class Packages(object):

    def get_install_order(self, depend):
        # type depend: graph list[list[int]]
        # rtype: str

        isInstalled = {}
        order = []
        order.append('')
        self.traverse_helper(depend, 0, isInstalled, order)

        return order[0]

    def traverse_helper(self, depend, crNode, isInstalled, order):
        # depend: graph list[list[int]]
        # crNode: int, index of current node
        # isInstalled: dictionary
        # order: output order string

        neighborList = depend[crNode]
        if not neighborList:
            if crNode not in isInstalled:
                order[0] += (str(crNode) + ' ')
                isInstalled[crNode] = True
            return

        for node in neighborList:
            self.traverse_helper(depend, node, isInstalled, order)

        order[0] += (str(crNode) + ' ')
        return

    def install(self, package):
        print("Install {0}".format(package))

def main():
    #graph = [[1, 2], [3, 4], [5], [], [5], []]
    graph = [[1], []]
    #graph = [[]]
    print('graph: {0}'.format(graph))

    obj = Packages()
    order = obj.get_install_order(graph)
    print('install order: {0}'.format(order))

if __name__ == '__main__':
    main()
