def sort_processes():
        # sort by cpu_percent
        top = {}
        time.sleep(0.1)
        for p in proc:
            # trigger cpu_percent() the second time for measurement
            top[p] = p.cpu_percent() / psutil.cpu_count()

        top_list = sorted(top.items(), key=lambda x: x[1])
        top10 = top_list[-10:]
        top10.reverse()

        return top10
