import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import shapiro
import argparse


def load_csv(path):
    f = open(path, "r")
    reader = csv.reader(f)
    data = []
    for row in reader:
        data += [row]
    header = data[0]
    return header, np.array(data[1:]).astype(np.float32)


def fig_demo(path):
    header, data = load_csv(path)
    idx_age = [i for i, t in enumerate(header) if t=='age']
    idx_bmi = [i for i, t in enumerate(header) if t=='BMI']
    age = data[:, idx_age]
    bmi = data[:, idx_bmi]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].hist(age, bins=10, edgecolor='black', color='#E69F00')   # Orange
    axes[0].set_title('a', fontweight='bold', loc='left')
    axes[0].set_xlabel('Age')
    axes[0].set_ylabel('Number of Participants')

    axes[1].hist(bmi, bins=10, edgecolor='black', color='#E69F00')
    axes[1].set_title('b', fontweight='bold', loc='left')
    axes[1].set_xlabel('BMI')
    axes[1].set_ylabel('Number of Participants')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('Fig_demo.png', dpi=300)
    return


def fig_sq(path):
    header, data = load_csv(path)
    idx_psqi = [i for i, t in enumerate(header) if t == 'PSQI']
    idx_ess = [i for i, t in enumerate(header) if t == 'ESS']
    psqi = data[:, idx_psqi]
    ess = data[:, idx_ess]

    fig, axes = plt.subplots(1, 3, figsize=(12, 5))
    n_good = np.sum(psqi <= 5)
    n_poor = np.sum(psqi > 5)
    axes[0].pie(
        [n_good, n_poor],
        labels=[f'Good SQ ({n_good})', f'Poor SQ ({n_poor})'],
        autopct='%1.1f%%',
        startangle=90,
        colors=['#009E73', '#E69F00']  # Green = good, Orange = poor
    )
    axes[0].set_title('a', fontweight='bold', loc='left')

    axes[1].hist(psqi, bins=10, edgecolor='black', color='#E69F00')
    axes[1].set_title('b', fontweight='bold', loc='left')
    axes[1].set_xlabel('PSQI')
    axes[1].set_ylabel('Number of Participants')

    axes[2].hist(ess, bins=10, edgecolor='black', color='#E69F00')
    axes[2].set_title('c', fontweight='bold', loc='left')
    axes[2].set_xlabel('ESS')
    axes[2].set_ylabel('Number of Participants')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('Fig_sq.png', dpi=300)
    return


def fig_sds(path):
    header, data = load_csv(path)
    idx_sds = [i for i, t in enumerate(header) if t == 'SDS']
    sds = data[:, idx_sds]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    n_normal = np.sum(sds < 50)
    n_mild = np.sum((sds >= 50) & (sds < 60))
    n_moderate = np.sum((sds >= 60) & (sds < 70))
    n_severe = np.sum(sds >= 70)
    axes[0].pie(
        [n_normal, n_mild],
        labels=[f'Normal ({n_normal})', f'Mild ({n_mild})'],
        autopct='%1.1f%%',
        startangle=90,
        colors=['#009E73', '#E69F00']  # Green = normal, Orange = mild
    )
    axes[0].set_title('a', fontweight='bold', loc='left')

    axes[1].hist(sds, bins=10, edgecolor='black', color='#E69F00')    # Orange
    axes[1].set_title('b', fontweight='bold', loc='left')
    axes[1].set_xlabel('SDS')
    axes[1].set_ylabel('Number of Participants')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('Fig_sds.png', dpi=300)
    return


def fig_brums(path):
    def getdata(name, data):
        idx = [i for i, t in enumerate(header) if t == name]
        value = data[:, idx]
        return value

    def plot_change(ax, emo):
        before = getdata(f'BRUMS_{emo}1', data)
        after = getdata(f'BRUMS_{emo}2', data)

        for b, a in zip(before, after):
            ax.plot([0, 1], [b, a], marker='o', color='#E69F00', alpha=0.7)  # Orange

            ax.set_xticks([0, 1])
            ax.set_xticklabels(['Before', 'After'])
            ax.set_ylabel(f'{emo}')
            ax.grid(alpha=0.3, linestyle='--')

    header, data = load_csv(path)
    fig, axes = plt.subplots(2, 4, figsize=(12, 7))
    plot_change(axes[0, 0], 'anger')
    plot_change(axes[0, 1], 'tension')
    plot_change(axes[0, 2], 'depression')
    plot_change(axes[0, 3], 'vigor')
    plot_change(axes[1, 0], 'fatigue')
    plot_change(axes[1, 1], 'confusion')
    plot_change(axes[1, 2], 'happy')
    plot_change(axes[1, 3], 'calmness')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('Fig_brums.png', dpi=300)
    return


def fig_stai(path):
    header, data = load_csv(path)
    idx_stai1 = [i for i, t in enumerate(header) if t == 'STAI1']
    idx_stai2 = [i for i, t in enumerate(header) if t == 'STAI2']
    before = data[:, idx_stai1]
    after = data[:, idx_stai2]

    fig, axes = plt.subplots(1, 3, figsize=(12, 5))

    axes[0].hist(before, bins=10, edgecolor='black', color='#E69F00')  # Orange
    axes[0].set_title('a', fontweight='bold', loc='left')
    axes[0].set_xlabel('STAI Before Sleep')
    axes[0].set_ylabel('Number of Participants')

    axes[1].hist(after, bins=10, edgecolor='black', color='#E69F00')
    axes[1].set_title('b', fontweight='bold', loc='left')
    axes[1].set_xlabel('STAI After Sleep')
    axes[1].set_ylabel('Number of Participants')

    axes[2].set_title('c', fontweight='bold', loc='left')
    for b, a in zip(before, after):
        axes[2].plot([0, 1], [b, a], marker='o', color='#E69F00', alpha=0.7)  # Orange

        axes[2].set_xticks([0, 1])
        axes[2].set_xticklabels(['Before', 'After'])
        axes[2].set_ylabel('STAI')
        axes[2].grid(alpha=0.3, linestyle='--')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('Fig_stai.png', dpi=300)
    return


def fig_hyp(path, sub):
    stage_map = {
        "WK": 0,
        "N1": 2,
        "N2": 3,
        "N3": 4,
        "REM": 1,
        "NS": None,  # disconnected / noise → 제외
        "": None
    }

    epochs = []
    stages = []

    with open(path, encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)

        for row in reader:
            stage = row[4].strip()  # Sleep Stage - mod
            if stage_map.get(stage) is None:
                continue

            epochs.append(int(row[0]))
            stages.append(stage_map[stage])

    if len(stages) == 0:
        print(f"No valid stages found for subject {sub}")
        return

    # ----- x축: 시간(hour) -----
    fs = 20
    t_hour = [(e - 1) * (30 / 3600) for e in epochs]

    # ----- plot -----
    plt.figure(figsize=(12, 8))
    plt.step(t_hour, stages, where="post")

    plt.yticks(
        [0, 1, 2, 3, 4],
        ["W", "REM", "N1", "N2", "N3"],
        fontsize=fs
    )
    plt.xlabel("Time (h)", fontsize=fs)
    plt.ylabel("Sleep Stage", fontsize=fs)

    plt.gca().invert_yaxis()
    plt.grid(alpha=0.3)
    max_hour = int(np.ceil(max(t_hour)))
    plt.xticks(range(0, max_hour + 1, 1), fontsize=fs)
    plt.xlim([0, max_hour])

    plt.tight_layout()
    plt.savefig(f'Fig_hyp{sub}.png', dpi=300)


def show(path, head):
    header, data = load_csv(path)
    idx = [i for i, t in enumerate(header) if t == head]
    item = data[:, idx]
    stat, p = shapiro(item)
    print(f"{head} :  {np.mean(item):.2f} +- {np.std(item):.2f} ({np.min(item)}-{np.max(item)}) (p = {p:.3f})")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--demo', action='store_true', help='Run fig_demo()')
    parser.add_argument('--sq', action='store_true', help='Run fig_sq()')
    parser.add_argument('--sds', action='store_true', help='Run fig_sds()')
    parser.add_argument('--brums', action='store_true', help='Run fig_brums()')
    parser.add_argument('--stai', action='store_true', help='Run fig_stai()')
    parser.add_argument('--hyp', type=int, help='Run fig_hyp(subject_id)')
    parser.add_argument('--show', type=str, help='Run show(HEAD)')

    args = parser.parse_args()

    any_flag = any([
        args.demo,
        args.sq,
        args.sds,
        args.brums,
        args.stai,
        args.hyp is not None,
        args.show is not None,
    ])

    path = 'D:\\Dropbox\\Dataset\\PsyPSG\\psychological assessments.csv'
    if not any_flag:
        fig_demo(path)
        fig_sq(path)
        fig_sds(path)
        fig_brums(path)
        fig_stai(path)
        path_sub = f'D:\\Dropbox\\Dataset\\PsyPSG\\hyps\\P323.hyp'
        fig_hyp(path_sub, 323)
        show(path, 'CFQ')
        show(path, 'age')
        return

    if args.demo:
        fig_demo(path)
    if args.sq:
        fig_sq(path)
    if args.sds:
        fig_sds(path)
    if args.brums:
        fig_brums(path)
    if args.stai:
        fig_stai(path)
    if args.hyp is not None:
        path_sub = f'D:\\Dropbox\\Dataset\\PsyPSG\\hyps\\P{args.hyp}.hyp'
        fig_hyp(path_sub, args.hyp)
    if args.show is not None:
        show(path, args.show)


if __name__ == '__main__':
    main()