from client import LlmGuidedTreeOfThoughtMonteCarloSearchClient

def main():
    client = LlmGuidedTreeOfThoughtMonteCarloSearchClient()
    res = client.explore_solution_tree('Solve Countdown target 432 with [25, 50, 75, 100, 3, 6]')
    print('Tree of Thought Searcher: ' + res['search_session_id'] + ' (' + str(res['nodes_explored_count']) + ' nodes)')
    print('Path Score: ' + str(res['best_path_heuristic_score']) + ' | Solution Verified: ' + str(res['solution_verdict_verified']))
    print('Optimal Trajectory Steps: ' + ' -> '.join(res['optimal_trajectory_steps'][:2]) + '...')
    print('Graph URL: ' + res['thought_tree_graph_url'])

if __name__ == '__main__':
    main()
