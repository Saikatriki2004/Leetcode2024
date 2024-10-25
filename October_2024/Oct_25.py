class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Step 1: Sort the folders lexicographically
        folder.sort()

        result = []  # To store the root folders

        # Step 2: Iterate through each folder in the sorted list
        for f in folder:
            # Check if the current folder is a subfolder of the last added folder
            if not result or not f.startswith(result[-1] + "/"):
                result.append(f)  # Add the folder to the result if it's not a subfolder

        return result
