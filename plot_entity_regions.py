import pandas as pd
import matplotlib.pyplot as plt


def read_file_entity(parent_entity: str):
    """
    Read from the dataset and create a dataframe that only contains the follower numbers and region of focus for actors
    belonging to parent_entity. It then returns this dataframe.
    """
    # Read from the dataset and create a dataframe
    df = pd.read_excel('CANIS_PRC_state_media_on_social_media_platforms-2023-11-03.xlsx')
    # Only store instances when the parent entity is parent_entity
    new_df = df.loc[df["Parent entity (English)"] == parent_entity]
    new_df = new_df.drop(
        ['Language', 'Name (English)', 'Name (Chinese)', 'Entity owner (English)', 'Parent entity (English)',
         'Entity owner (Chinese)', 'Parent entity (Chinese)', 'X (Twitter) handle', 'X (Twitter) URL', 'Facebook page',
         'Facebook URL', 'Threads account', 'Threads URL', 'YouTube account', 'YouTube URL', 'TikTok account',
         'TikTok URL', 'Instagram URL', 'Instragram page'], axis=1)
    return new_df


def group_df(dropped_df):
    """
    Group the given dataframe together based on region of focus and sum up all the social media follower numbers for
    each region. Returns the dataframe where the index is the region of focus and containing the total follower numbers
    of all actors in each region
    """
    # Group the dataframe by the Region of Focus and sum up all the values
    grouped = dropped_df.groupby(['Region of Focus']).sum()
    # Create a new column that stores the total social media followers
    grouped["Social Media Followers"] = grouped[
        ['X (Twitter) Follower #', 'Facebook Follower #', 'Instagram Follower #', 'Threads Follower #',
         'YouTube Subscriber #', 'TikTok Subscriber #']].sum(axis=1)
    final = grouped.drop(
        ['X (Twitter) Follower #', 'Facebook Follower #', 'Instagram Follower #', 'Threads Follower #',
         'YouTube Subscriber #', 'TikTok Subscriber #'], axis=1)
    final = final.sort_values(by=['Social Media Followers'])
    return final


def plot(final, n, parent_entity):
    """
    Plot a lollipop plot showing the total social media followers for each region for a given entity using the final
    dataframe. Only shows the n regions with the most followers
    """

    if len(final.index) >= n:
        end = len(final.index) - n
        final = final.drop(index=final.index[:end], axis=0)
    values = final['Social Media Followers']
    my_range = range(1, len(final.index) + 1)

    # Draw the lollipop plot
    plt.hlines(y=my_range, xmin=0, xmax=values, color='skyblue')
    plt.plot(values, my_range, "D")
    plt.yticks(my_range, final.index)
    plt.xscale("log")

    # Add labels
    plt.xlabel("Total Social Media Followers")
    plt.ylabel("Region of Focus")
    plt.title("Total Followers of Actors - " + parent_entity)

    # Add the values of each line
    for i in range(len(final.index)):
        value = final.iloc[i]['Social Media Followers']
        value_to_print = value / (10 ** 6)
        if value_to_print > 1:
            plt.text(value + 0.36 * value, i + 1, str(round(value_to_print, 1)) + " million")
        else:
            plt.text(value + 0.2 * value, i + 1, str(round(value_to_print * 1000, 1)) + " thousand")

    plt.xlim(0, max(values) * 1.1)
    plt.show()


if __name__ == "__main__":
    entity = input("Enter the parent entity")
    df = read_file_entity(entity)
    final_df = group_df(df)
    plot(final_df, 10, entity)
