"""
Generate the class assignments for open/neither/closed conformations.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import operator

plt.style.use('/Users/wmd122/github/wedap/styles/default.mplstyle')

class Gen_Class_Assignments:

    def __init__(self, c1_bounds=60, c2_bounds=35, c1_label="closed", c2_label="open",
                 coord_data_file="all_pc.dat",
                 out_filename="class_assignments.txt"):
        """
        Parameters
        ----------
        # TODO: for now just doing this manually
        # TODO: could expand this to unpack input more robustly
        c1_bounds, c2_bounds : list or tuple of 3 items
            Each bounds is 3 items in the following order:
                - a lower bound float
                - a comparison operator input as a str (e.g. '<=')
                - a upper bound float
        c1_label, c2_label : str
            Label for the corresponding state assignment.
        coord_data_file : str
            Path to the file of calculated data for state assignments.
        out_filename : str
            Name of the output class assignment results file.
        """
        # import the rmsd and o_angle data files, only the data col not frames
        # TODO: eventually could make arg for multiple files and indices
        self.coord1 = np.loadtxt(coord_data_file)[:,1]
        self.coord2 = np.loadtxt(coord_data_file)[:,0]

        self.c1_bounds = c1_bounds
        self.c2_bounds = c2_bounds
        self.c1_label = c1_label
        self.c2_label = c2_label
        self.out_filename = out_filename

    # TODO: could expand this to unpack input more robustly
    @staticmethod
    def evaluate_expression(expression):
        # Unpack the expression
        operand1, operator_str, operand2 = expression

        # Map the operator string to the corresponding operator function
        operator_func = {
            '<': operator.lt,
            '<=': operator.le,
            '==': operator.eq,
            '!=': operator.ne,
            '>': operator.gt,
            '>=': operator.ge,
        }.get(operator_str)

        if operator_func is None:
            raise ValueError(f"Unsupported operator: {operator_str}")

        return operand1, operator_func, operand2

    def gen_class_assignments(self, save=True):
        """
        Parameters
        ----------
        save : bool
            Optionally save the class assigments.
        """
        # array of frame labels initialized with "neither"
        # structured array with a variable-length string field
        # otherwise the default dtype=str only holds a single char
        labels = np.zeros(len(self.coord1), dtype=[("label", "U10")])

        # set the default label to "neither"
        labels["label"] = "neither"

        # assign labels from element wise conditions
        labels[(self.coord1 < self.c1_bounds) & (self.coord2 < self.c2_bounds)] \
            = self.c1_label
        labels[(self.coord1 > self.c1_bounds) & (self.coord2 > self.c2_bounds)] \
            = self.c2_label

        # # the above excludes the sides of the dist, here lets do a full binary classification
        # labels["label"] = self.c2_label # all to open and then label closed only
        # labels[(self.coord1 < self.c1_bounds) & (self.coord2 < self.c2_bounds)] \
        #     = self.c1_label

        # save the labeled class assignments structured array
        if save:
            np.savetxt(self.out_filename, labels, fmt="%s")

        self.labels = labels
        return labels

    def state_assign_plot(self):
        # make a plot of the class assignments
        # Map text labels to numerical values
        label_mapping = {self.c1_label: 0, 'neither': 1, self.c2_label: 2}
        #label_mapping = {self.c1_label: 0, self.c2_label: 2}
        numerical_labels = np.array([label_mapping[label] for label in self.labels['label']])

        # Create a colormap
        # colors = ['#DEE11E', '#1EDEE1', '#E11EDE']
        #colors = ['#1594EA', '#989C96', '#EA6B15']
        # colors = ['#DEE11E', '#E11EDE']
        # colors = ['#1594EA', '#EA6B15']
        #colors = ['#1f77b4', '#ff7f0e']
        colors = ['#1f77b4', '#989C96', '#ff7f0e']
        cmap = ListedColormap(colors)

        # Scatter plot
        plt.scatter(self.coord1, self.coord2, c=numerical_labels, cmap=cmap, s=0.1, alpha=0.8)

        # Add colorbar
        cbar = plt.colorbar()
        cbar.set_ticks([0, 1, 2])
        #cbar.set_ticks([0.5, 1.5])
        cbar.set_ticklabels(list(label_mapping.keys()))

        # add state label lines
        # [plt.axhline(y=i, linestyle='--', color='k') for i in [9, 16]]
        # [plt.axvline(x=i, linestyle='--', color='k') for i in [1.7, 3.7]]
        #plt.axhline(y=16, xmax=(1.7/6), linestyle='--', color='k')
        #plt.axhline(y=9, xmin=(3.7/6), linestyle='--', color='k')
        #plt.axvline(x=1.7, ymin=(16/34), linestyle='--', color='k')
        #plt.axvline(x=3.7, ymax=(9/34), linestyle='--', color='k')

        # lines = [self.c1_bounds, self.c2_bounds]
        # [plt.axhline(y=i, linestyle='--', color='k') for i in lines]
        # [plt.axvline(x=i, linestyle='--', color='k') for i in lines]
        plt.axhline(y=self.c2_bounds, linestyle='--', color='k')
        plt.axvline(x=self.c1_bounds, linestyle='--', color='k')


        # formatting
        plt.xlim(30, 90)
        plt.ylim(20, 55)
        plt.xlabel("Opening Angle (°)")
        plt.ylabel("Cu(II)-Cu(II) Distance ($\AA$)")
        #plt.title("CA-CTD State Labels")

        plt.tight_layout()
        plt.savefig("state_labels_withneither.pdf")
        plt.show()

if __name__ == "__main__":
    gen = Gen_Class_Assignments(coord_data_file="all_pc.dat", out_filename="class_assignments_withneither.txt")
    gen.gen_class_assignments()
    gen.state_assign_plot()
